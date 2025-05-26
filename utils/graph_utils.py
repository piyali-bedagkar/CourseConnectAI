import networkx as nx
from pyvis.network import Network
from streamlit.components.v1 import html
import tempfile
import os
import random
import streamlit as st


def build_graph(entities):
    G = nx.Graph()
    for ent in entities:
        if len(ent) == 3:
            src, rel, tgt = ent
            G.add_node(src)
            G.add_node(tgt)
            G.add_edge(src, tgt, label=rel)
    return G

def generate_graph_html(G):
    net = Network(height="600px", width="100%", notebook=False, directed=False)
    net.barnes_hut()

    node_colors = {}
    for node in G.nodes():
        if node not in node_colors:
            node_colors[node] = "#{:06x}".format(random.randint(0x888888, 0xFFFFFF))

        net.add_node(
            node,
            label=node,
            title=node,
            color=node_colors[node],
            font={"size": 22}
        )

    for src, tgt, data in G.edges(data=True):
        rel = data.get("label", "")
        net.add_edge(src, tgt, title=rel)

    html_code = net.generate_html()
    html_code = html_code.replace("network = new vis.Network(container, data, options);", """
    network = new vis.Network(container, data, options);
    window.network = network;
    window.nodes = data.nodes;
    """)
    return html_code


def visualize_graph(G):
    net = Network(
        height="1000px",
        width="100%",
        notebook=False,
        directed=False,
        bgcolor="#000000",
        font_color="white"
    )
    net.barnes_hut()

    node_colors = {}
    for node in G.nodes():
        if node not in node_colors:
            node_colors[node] = "#{:06x}".format(random.randint(0x888888, 0xFFFFFF))

        net.add_node(
            node,
            label=node,
            title=node,
            color=node_colors[node],
            font={"size": 22}
        )

    for src, tgt, data in G.edges(data=True):
        rel = data.get("label", "")
        net.add_edge(src, tgt, title=rel)

    # Save graph
    tmp_dir = tempfile.gettempdir()
    path = os.path.join(tmp_dir, "graph.html")
    net.save_graph(path)

    with open(path, "r", encoding="utf-8") as f:
        base_html = f.read()

        # Inject window.network and window.nodes
        base_html = base_html.replace(
            "network = new vis.Network(container, data, options);",
            "network = new vis.Network(container, data, options);\nwindow.network = network;\nwindow.nodes = data.nodes;"
        )

        # Clean PyVis boilerplate
        base_html = base_html.replace("Loading...", "")
        base_html = base_html.replace(
            "<body",
            "<body style='margin:0; padding:0; background-color:black;'"
        ).replace(
            "<iframe",
            "<iframe style='border: none !important; background-color: black !important; outline: none !important; box-shadow: none !important; width: 100%; display: block;'"
        ).replace(
            "border: 1px solid lightgray;", ""
        ).replace("frameborder=\"1\"", "frameborder=\"0\"").replace("border:1px solid #ddd;", "")

        # Full page HTML with stats only (search bar removed)
        full_html = f"""
    <div style="position: relative; background-color: black; width: 100%; overflow: hidden;">
        <div style="position: absolute; top: 150px; left: 30px; background-color: rgba(0,0,0,0.7); padding: 20px 25px; border-radius: 10px; z-index: 10; color: white;">
            <h2 style="margin-top: 0;">Knowledge Graph</h2>
            <ul style="font-size:16px; line-height:2; list-style: none; padding-left: 0;">
                <li><b>Total Courses:</b> 124</li>
                <li><b>Total Professors:</b> 47</li>
                <li><b>Avg. Connections:</b> 34.4</li>
            </ul>
        </div>
        {base_html}
    </div>
    """

    html(full_html, height=1000, scrolling=False)

## Data Manager

This project builds a complete understanding of how modern web mapping systems work by constructing a vector tile pipeline from scratch and then comparing it to a production-grade tool: Tippecanoe.

Instead of starting with the tool, we first build the system manually across a sequence of notebooks. This lets us understand every component — from geometric simplification to spatial indexing to level-of-detail (LOD) selection — before replacing it with a single optimized command.

The goal is not to “reinvent Tippecanoe,” but to understand exactly what problems it solves, what tradeoffs it makes, and why it is used in production systems like Mapbox and OpenStreetMap-based applications.


## Notebooks

Consists of 8 modules of 21 notebooks
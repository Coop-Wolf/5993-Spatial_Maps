# Data Manager — Micro Lesson Roadmap

These micro lessons are designed to build the skills needed for the **Data Manager** project one concept at a time. The central problem is a real one: a 40MB world railroad GeoJSON file is far too large to load on every map pan and zoom. These lessons build — from scratch — the tools needed to solve that problem intelligently. A library that solves all of this already exists. We are building the small version first.

The general progression is:

```text
Data Exploration → Douglas-Peucker Simplification → Generating LOD Files
→ Bounding Box Culling → Spatial Grid Index → Zoom-Driven Layer Switching
→ Putting It All Together → The Library Version
```

| #   | Folder                                             | Description                                                             | Notebooks |
| --- | -------------------------------------------------- | ----------------------------------------------------------------------- | :-------: |
| 00  | [00-Data_Exploration](00-Data_Exploration)         | Load and inspect the raw GeoJSON; measure the problem                   |     2     |
| 01  | [01-Douglas_Peucker](01-Douglas_Peucker)           | Understand and implement the core simplification algorithm              |     3     |
| 02  | [02-LOD_Generation](02-LOD_Generation)             | Apply simplification at multiple tolerances; write LOD output files     |     3     |
| 03  | [03-Bounding_Box_Culling](03-Bounding_Box_Culling) | Filter features to the visible viewport using bounding box intersection |     3     |
| 04  | [04-Spatial_Grid_Index](04-Spatial_Grid_Index)     | Speed up culling with a simple grid-based spatial index                 |     3     |
| 05  | [05-Zoom_Layer_Switching](05-Zoom_Layer_Switching) | Select and load the correct LOD file based on zoom level                |     2     |
| 06  | [06-Putting_It_Together](06-Putting_It_Together)   | Combine all components into a working interactive railroad viewer       |     2     |
| 07  | [07-The_Library_Version](07-The_Library_Version)   | Reproduce the same result using `tippecanoe` and vector tiles           |     3     |

---

## 00 — Data Exploration

### Goal

Understand the raw data before touching it. Measure the problem.

### Students will practice

- loading a large GeoJSON file and inspecting its structure
- counting features, checking geometry types, and reading properties
- computing a bounding box over the full dataset
- timing a naive load-and-display attempt to feel the performance problem firsthand

### Why this matters

You cannot design a solution to a problem you have not measured. This notebook makes the case for everything that follows.

---

## 01 — Douglas-Peucker Simplification

### Goal

Understand and implement the algorithm that reduces the number of points in a line while preserving its shape.

### Students will practice

- tracing the Douglas-Peucker algorithm by hand on a small example
- implementing the recursive algorithm in Python
- verifying their output against `shapely.simplify()`
- experimenting with different `epsilon` values and observing the tradeoff

### Why this matters

This is the core concept. Every LOD pipeline, every simplification tool, every geometry compression scheme rests on ideas like this one. Students who can build a toy version understand the tool. Students who only import it do not.

---

## 02 — LOD File Generation

### Goal

Apply the simplification algorithm at four tolerance levels and write the output files.

### Students will practice

- designing an epsilon-to-zoom-level mapping
- writing a pipeline that processes all features and applies D-P at each level
- measuring how feature count and file size change at each level
- writing four output GeoJSON files: `coarse`, `medium`, `fine`, `extra_fine`

### Why this matters

This is the first time the algorithm is applied at scale. Students see the connection between epsilon, visual fidelity, and file size — and make deliberate tradeoffs.

| Level      | Zoom Range | Epsilon (degrees) | Approx. Output Size |
| ---------- | ---------- | ----------------- | ------------------- |
| Coarse     | 1–3        | ~1.0              | ~500 KB             |
| Medium     | 4–6        | ~0.1              | ~2–3 MB             |
| Fine       | 7–10       | ~0.01             | ~8–10 MB            |
| Extra Fine | 11+        | ~0.001            | ~20–25 MB           |

---

## 03 — Bounding Box Culling

### Goal

Eliminate features that fall entirely outside the current map viewport before rendering.

### Students will practice

- computing an axis-aligned bounding box for any GeoJSON feature
- writing a bounding box intersection test
- applying the filter to a LOD file and measuring how many features are removed
- displaying only the culled result on a map

### Why this matters

Even the simplified `fine` layer has thousands of features spread across the world. When you are looking at Kansas, you do not need Siberia. This lesson teaches spatial filtering as a performance tool.

---

## 04 — Spatial Grid Index

### Goal

Speed up viewport culling by avoiding a full linear scan of every feature.

### Students will practice

- dividing the world into a uniform grid of cells
- pre-assigning features to the cells they overlap
- querying only the cells that intersect the current viewport
- comparing query time with and without the index

### Why this matters

Iterating every feature for every pan event is O(n). A spatial index reduces the query to a small subset. Students learn _why_ spatial indexes exist — not just that they do. This is the conceptual precursor to R-trees, quadtrees, and every other spatial data structure they will encounter later.

---

## 05 — Zoom-Driven Layer Switching

### Goal

Select and load the correct LOD file in response to zoom level changes.

### Students will practice

- registering a zoom event handler in ipyleaflet
- writing a `get_layer(zoom)` decision function
- dynamically swapping the active GeoJSON layer on the map
- combining layer switching with bounding box culling

### Why this matters

This is the moment the pieces connect. The map now behaves like a real mapping application: different data at different scales, loaded on demand.

---

## 06 — Putting It All Together

### Goal

Combine every component into a working interactive railroad viewer.

### Students will practice

- wiring up D-P simplified LOD files, viewport culling, and zoom-driven switching into one clean notebook
- identifying which parts are slow and which are fast
- observing where the remaining pain points are (reload time, layer flicker, file I/O)
- documenting the design decisions they made

### Why this matters

Students see a working system built entirely from components they understand. This is the completion moment — and also the setup for the next lesson.

---

## 07 — The Library Version

### Goal

Reproduce the LOD pipeline using `tippecanoe` and understand what it automates.

### Students will practice

- installing and running `tippecanoe` on the raw GeoJSON
- inspecting the output: `.pmtiles` or `.mbtiles` format, tile pyramid structure
- loading vector tiles in ipyleaflet
- comparing the library output visually and structurally against their handbuilt version

### Why this matters

At this point students have built the small version and felt every tradeoff. The library version is no longer a black box. Students can now answer: _what did tippecanoe just save us from?_ — and name specific things, because they built those things.

---
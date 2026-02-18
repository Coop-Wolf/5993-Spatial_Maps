# 🚀 Project 01: Missile Geometry 101  

## 🧠 Scenario

You are a **Spatial Defense Analyst** working for the **World Defense Organization**.

Earth is under threat from **non-human entities**:
- Alien spacecraft
- Orbital kinetic weapons
- High-altitude airborne platforms
- Kaiju-class ground threats (yes, really)

The mission is to **analyze geometry**.

Specifically:
- Where threats are coming from
- Where they are going
- What they intersect
- Who (or what) might be affected

---

## ☄️ Incoming Threats (Simulated)

Each threat has:

- `origin_lat`
- `origin_lon`
- `bearing` (degrees)
- `speed` (km per hour)
- `launch_time`
- `threat_type`
  - `"alien"`
  - `"orbital"`
  - `"airborne"`
  - `"kaiju"`

---

## 📍 Milestone 1 — Plot the World

**Goal:** Prove you can load and visualize spatial data.

### Tasks
- Load a world countries shapefile (or GeoJSON)
- Display it using Folium
- Add your base location as a point marker

---

## 📏 Milestone 2 — Distance & Bearing

**Goal:** Reason about spatial relationships numerically *and* visually.

### Tasks
- Compute the distance from each threat origin to your base
- Identify the **closest threat**
- Display threat origins as points

---

## ➖ Milestone 3 — Trajectories (Point → Line)

**Goal:** Turn motion into geometry.

### Tasks
- For each threat:
  - Compute a **destination point** after a fixed time interval
  - Generate intermediate points
  - Construct a `LineString` trajectory
- Plot trajectories on the map

### Visual Expectation
You should clearly see:
- Where threats started
- Where they are headed
- How paths differ by bearing and speed

---

## 🧱 Milestone 4 — Intersections & Borders

**Goal:** Determine what the threats interact with.

### Tasks
- Determine:
  - Which country polygons each trajectory **intersects**
  - Whether a trajectory passes **within a threshold distance** of your base
- Highlight intersected countries on the map

### Spatial Relationships Used
- `intersects`
- `within`
- distance thresholds

---

## 💥 Milestone 5 — Damage Zones (The Bridge)

**Goal:** Prepare data for the next project.

### Tasks
- Create a **buffer zone** around each trajectory endpoint
- Buffer size depends on `threat_type`
- Determine which countries fall within damage zones


---


#### 📂 Project File Overview

| Files / Folders                  | Description                                                      |
|----------------------------------|------------------------------------------------------------------|
| **Screenshots/**                 | Stores screenshots of maps for each milestone.                   |
| **json/**                        | Stores countries, and threats json files                         |
| **html/**                        | Stores html files of generated maps.                             |
| **config.py**                    | Contains global configuration variables.                         |
| **Missile_Geometry.ipynb**       | Main notebook for Assignment.                                    |
| **README.md**                    | Project documentation and instructions.                          |

---

#### Project thoughts

This was my first time working on a project like this, and it came with a fairly steep learning curve. Learning how to use Folium and Shapely took time, especially as I worked to understand how geospatial data and geometry objects functioned behind the scenes. As a result, there was a good amount of debugging and learning as I went, which challenged me but also helped me grow. Despite that, I really enjoyed the project. It was rewarding to visualize the final output and see the threats mapped out along with their distances from the home base, which made the entire experience both engaging and satisfying.
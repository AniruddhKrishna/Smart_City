# Smart_City <br>
The repository for the Shaastra Smart City Hackathon where we claimed 1st prize among 623 participants.

Welcome to the Water Quality Monitoring & Analysis System repository! This project provides a comprehensive solution for real-time monitoring, visualization, and intelligent analysis of water quality in drainage systems. It combines IoT data simulation, a live dashboard, computer vision for object detection, and a smart retrieval-augmented QA system.

Project Structure
backend.py: FastAPI backend simulating IoT water sensor data and serving it via REST and WebSocket.

dashboard.py: Streamlit dashboard for real-time visualization and alerting of water quality parameters.

object_detection_drainage.py: Computer vision script for detecting objects (e.g., stones) in drainage images.

smartrag.py: Smart Retrieval-Augmented Generation (RAG) system for answering questions based on local documents using LLMs and vector search.

Features Overview
1. Real-Time IoT Water Data Backend (backend.py)
Simulates water sensor data: Generates random but realistic values for temperature, pH, turbidity, flow rate, and dissolved oxygen.

REST API: Simple endpoint (/) to verify the backend is running.

WebSocket streaming: Live data pushed every second to connected clients for real-time updates.

CORS enabled: Allows cross-origin requests, making integration with web dashboards easy.

Extensible: Replace the simulation logic with actual IoT sensor integration as needed.

2. Interactive Dashboard (dashboard.py)
Built with Streamlit: Easy to deploy and use in a browser.

Live visualization: Displays current sensor readings as gauges for temperature, pH, and dissolved oxygen.

Historical trends: Plots time series of recent readings for trend analysis.

Alerts: Highlights parameters that are out of acceptable range.

Raw data table: Shows recent sensor readings for transparency.

Auto-refresh: Updates every 5 seconds for near real-time monitoring.

Thresholds: Configurable acceptable ranges for each parameter.

3. Object Detection in Drainage Images (object_detection_drainage.py)
Image processing pipeline:

Reads an image of drainage water.

Enhances contrast, applies Gaussian blur, and detects edges.

Finds and filters contours to detect large objects (e.g., stones) in the water.

Visualizes results by overlaying detected contours on the original image.

Use case: Helps identify physical blockages or debris in drainage systems using computer vision.

4. Smart Retrieval-Augmented QA System (smartrag.py)
Document ingestion: Loads and splits local .txt documents into manageable chunks.

Vector store: Uses FAISS and sentence-transformers to create a searchable embedding database.

LLM integration: Utilizes a local GPT-2 model for generating answers.

Retrieval-augmented generation: Answers user questions by retrieving relevant document chunks and generating context-aware responses.

Streamlit integration: Can be extended for web-based QA interfaces.

Highly modular: Easily swap in larger LLMs or different embedding models as needed.

How It All Fits Together
Component	Purpose	Technologies
backend.py	Simulates and streams water sensor data	FastAPI, Python
dashboard.py	Visualizes and monitors water data in real-time	Streamlit, Plotly
object_detection_drainage.py	Detects objects in drainage images	OpenCV, NumPy
smartrag.py	Answers questions using local docs + LLMs	LangChain, FAISS, Transformers
Getting Started
Backend:

Run backend.py to start the FastAPI server (default: localhost:8000).

Dashboard:

Run dashboard.py with Streamlit to launch the dashboard in your browser.

Object Detection:

Run object_detection_drainage.py in an environment with OpenCV and a sample image.

Smart RAG:

Run smartrag.py to set up the QA system and interact via the terminal.

Customization & Extension
Replace simulated data in backend.py and dashboard.py with actual IoT sensor readings for deployment.

Adapt the object detection script for different types of blockages or debris.

Expand the smart RAG system with additional documents or more powerful language models for advanced analytics and reporting.

Use Cases
Continuous monitoring of water quality in drainage or industrial systems.

Early detection of anomalies and physical obstructions.

Intelligent querying and reporting based on historical records and documentation.

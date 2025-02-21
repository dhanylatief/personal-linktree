# Use the official Streamlit image from the Docker Hub
FROM streamlit/streamlit:latest

# Set the working directory to /app
WORKDIR /app

# Copy everything to the /app directory
COPY . /app

# Expose the port Streamlit is running on
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "streamlit_app.py"]
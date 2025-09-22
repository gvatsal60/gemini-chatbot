# ##########################################################################
# File: Dockerfile
# Author: Vatsal Gupta (gvatsal60)
# Date: 21-Sep-2025
# Description: Dockerfile for a Streamlit application using UV base image.
# ##########################################################################

# ##########################################################################
# License
# ##########################################################################
# This Dockerfile is licensed under the Apache 2.0 License.
# License information should be updated as necessary.
# ##########################################################################

# ##########################################################################
# Base Image
# ##########################################################################
# Stage 1: Builder - Install dependencies
FROM python:3.12-slim AS builder

# ##########################################################################
# Maintainer
# ##########################################################################
LABEL maintainer="Vatsal Gupta (gvatsal60)"

# ##########################################################################
# Set Working Directory
# ##########################################################################
WORKDIR /app

# ##########################################################################
# Copy Files
# ##########################################################################
# Copy requirements and install them
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ .

# Stage 2: Runtime - Create the distroless image
FROM gcr.io/distroless/python3.12:nonroot

WORKDIR /app

# Copy installed packages and application code from the builder stage
COPY --from=builder /root/.local /usr/.local
COPY --from=builder /app .

# Add the user's local bin directory to the PATH
ENV PATH=/usr/.local/bin:$PATH

# ##########################################################################
# Expose Port
# ##########################################################################
EXPOSE 8501

# ##########################################################################
# Command to Run
# ##########################################################################
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--browser.gatherUsageStats=false"]

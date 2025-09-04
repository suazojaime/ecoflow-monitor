FROM python:3.11-slim

# Install cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python script and requirements
COPY *.py requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy cronjob file and install it
COPY cronjob /etc/cron.d/monitor-cron
RUN chmod 0644 /etc/cron.d/monitor-cron && \
    crontab /etc/cron.d/monitor-cron

# Create log file
RUN touch /var/log/cron.log

# Start cron and keep container running
CMD cron && tail -f /var/log/cron.log

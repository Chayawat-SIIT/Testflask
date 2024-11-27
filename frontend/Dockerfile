# Use the official Nginx image as the base image
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Remove the default Nginx static files
RUN rm -rf ./*

# Copy the static assets and template files
COPY static /usr/share/nginx/html/static
COPY template /usr/share/nginx/html/template

# Copy the Nginx configuration file if needed (optional, for custom routing or settings)
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for serving HTTP traffic
EXPOSE 80
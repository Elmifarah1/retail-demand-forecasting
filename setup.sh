cat > setup.sh << 'EOF'
mkdir -p ~/.streamlit
cat > ~/.streamlit/config.toml << EOC
[server]
headless = true
port = $PORT
enableCORS = false
enableXsrfProtection = false
address = "0.0.0.0"
EOC
EOF

chmod +x setup.sh
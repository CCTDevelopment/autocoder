from app import create_app  # Absolute import

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from website import create_app

app = create_app()

if __name__ == '__main__':
    # Permet à Flask de s'exécuter sur n'importe quelle interface réseau
    app.run(debug=True, host='0.0.0.0', port=5000)

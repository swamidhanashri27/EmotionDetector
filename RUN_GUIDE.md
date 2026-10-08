# Run Guide

1. Create a virtual environment:
   python -m venv venv

2. Activate it on Windows:
   venv\Scripts\activate

3. Install packages:
   pip install -r requirements.txt

4. Run unit tests:
   python -m unittest test_emotion_detection.py

5. Run Flask:
   python server.py

6. Open:
   http://127.0.0.1:5000/

7. Static analysis:
   pylint server.py

Note: the Watson Skills Network endpoint must be reachable for live Watson results.
The included unit tests mock the API response so the tests can run without network access.

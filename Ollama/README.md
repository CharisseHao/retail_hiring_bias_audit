# Retail Hiring Suggestions - Age x Names x Education Audit (Ollama)

Ollama and luigi-based orchestration for single-prompt permutation experiments

Instructions:
1. Go to [ollama.com](https://ollama.com/) and download the Ollama application
2. Launch Ollama by clicking the application or run `ollama start` in a terminal
3. Run the following commands in a terminal:
<!-- - `ollama pull llama2:7b-chat-q4_K_M` -->
- `ollama pull llama3:8b-instruct-q4_K_M`
- `pip install -r requirements.txt`
- `python3 run_luigi.py retail_hiring.yml`
  - for verbose debugging: `python3 run_luigi.py --verbose retail_hiring.yml`
  - to replace existing output file (specified in yml), otherwise will resume: `python3 run_luigi.py --replace retail_hiring.yml`
4. (Optional) To run the unit tests for the `parse_percentage` function in `percentparser.py`, use the following command:<br />
  `python tests/test_parse_percentage.py`

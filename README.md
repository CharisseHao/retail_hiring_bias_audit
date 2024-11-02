# DSC180A-Capstone-Q1

Ollama and luigi-based orchestration for single-prompt permutation experiments
<!-- - `mmlu`: Ollama-based orchestration for permuting pre- and post-question instructions for the MMLU and MMLUPro question answering benchmarks -->

Instructions:
1. Go to ollama.com and download ollama
2. Run the following lines in terminal:
- `ollama pull llama2:7b-chat-q4_K_M`
- `ollama pull llama3:8b-instruct-q4_K_M`
- `pip install -r requirements.txt`
- `python3 run_luigi.py retail_hiring.yml`
  - for verbose debugging: `python3 run_luigi.py --verbose retail_hiring.yml`
  - to rerun, delete the `data` folder and run `python3 run_luigi.py retail_hiring.yml` again 
  <!-- - to replace existing output file (specified in yml), otherwise will resume: `python3 run_luigi.py --replace retail_hiring.yml` -->
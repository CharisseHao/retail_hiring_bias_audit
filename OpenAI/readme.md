# Retail Hiring Suggestions - Age x Names x Education audit (OpenAI/vllm)

OpenAI and vllm-based orchestration for bulk batch processing and analysis

Descriptions and Instructions:
- `step1_prompt_bulk_generator.ipynb`: inputs `input_data\audit_names.xlsx` and generates prompts in OpenAI Batch `.jsonl` format
    - These must be submitted to the [OpenAI Batch API](https://platform.openai.com/batches) or for open-weight models, can be submitted with [vllm batch](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_openai.md). 
    - The are files large, so they are stored as `.zip` in GitHub. To replicate this with OpenAI or vllm, unzip these files and only submit the raw `.jsonl` file.
    - Prompt submission instructions:
        1. Download Batchwizard using:<br />
            `pip install batchwizard`
        2. Set API key, replacing `YOUR_SECRET_KEY` with your API key:<br />
            `batchwizard configure --set-key YOUR_SECRET_KEY`
        3. Change to the `input_data/batch_requests` directory
        4. Submit prompt file:<br />
            `batchwizard process age_name_edu_gpt-4o-mini-2024-07-18.jsonl`
    - OpenAI or vllm returns a result `.jsonl` file. 
        - Download the results, replacing `JOB_ID` with the Job ID of the result you want to download:<br />
            `batchwizard download JOB_ID`, 
        - Place the downloaded files in the `output_data` folder.
- `step2_parse_clean_data.ipynb`: reads all `.jsonl` or `.jsonl.zip` files in the `output_data` folder, parses the percent value from the responses, and stores all results in `processed_data/age_name_edu_data.csv.zip`
- `step3_analysis.ipynb`: reads `processed_data/age_name_edu_data.csv.zip` and performs the analyses
- `Tests` folder: contains unit tests for the `parse_percentage` function in `percentparser.py`
    - To run tests, use the following command:<br />
        `python tests/test_parse_percentage.py`

from huggingface_hub import HfApi

api = HfApi()

api.upload_folder(
    folder_path="saves/llama3-8b/lora/dpo",
    repo_id="Huy227/adapter_v11",
    repo_type="model",
)

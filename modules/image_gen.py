import requests, os, base64
from config import CONFIG

def generate_realistic_image(name, config=CONFIG):
    prompt = config["prompt_template"].format(name=name)
    output_dir = os.path.join(config["output_dir"], "images")
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{name}.png")
    response = requests.post(
        "https://api.runpod.ai/v2/stable-diffusion/run",
        headers={"Authorization": f"Bearer {config['stable_diffusion_api']}"},
        json={"prompt": prompt}
    )
    data = response.json()
    image_data = data.get("image_base64")
    if not image_data:
        raise Exception(f"Image generation failed for {name}")
    with open(out_path, "wb") as f:
        f.write(base64.b64decode(image_data))
    return out_path
import replicate
import os

# Ensure your API token is loaded from the .env file
os.environ["REPLICATE_API_TOKEN"] = "r8_2tWRxCB6i8tAG66zPpEQgmtovzRWde30K67Eb"

output = replicate.run(
    "amjad72majeed/video-generation",
    input={"prompt": "A futuristic city skyline at sunset"}
)

print("Model Output:", output)
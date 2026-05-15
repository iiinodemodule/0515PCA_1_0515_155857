import torch


# Inline algorithm logic here (helper functions from source)
def adjust_brightness(image, strength):
    # 變數名稱必須與 INPUT_TYPES 中宣告的名稱一致
    # image 為 torch.Tensor，shape: [B, H, W, C]
    result = torch.clamp(image * strength, 0.0, 1.0)

    # 回傳值必須是 Tuple 格式
    return (result,)


class BrightnessAdjustNode:
    CATEGORY = "0515_155857自訂演算法/PCA1"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "strength": (
                    "FLOAT",
                    {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.1},
                ),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "execute"

    def execute(self, image, strength):
        return adjust_brightness(image, strength)

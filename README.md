# JPEG Compression in Python

This project implements a simplified JPEG compression and decompression pipeline in Python.

The goal is to study the main steps involved in image compression, including color-space conversion, chroma subsampling, block processing, DCT, quantization, zig-zag scanning, run-length encoding, Huffman coding, image reconstruction, and quality evaluation.

## Features

- RGB to YCbCr conversion
- 4:2:0 chroma subsampling
- 8x8 block division
- Discrete Cosine Transform (DCT)
- Quantization using different quantization matrices
- Differential Pulse Code Modulation (DPCM) for DC coefficients
- Zig-zag scanning
- Zero run-length encoding
- Huffman coding and decoding
- JPEG-like decompression
- PSNR and SSIM quality evaluation
- Compression ratio and bits-per-pixel analysis

## Project Structure

```text
jpeg-compression-python/
├── data/
│   └── input/
│       └── sample_image.png
├── results/
│   └── images/
│       └── sample_original.png
├── jpeg_compression.ipynb
├── huffman.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/YOUR-USERNAME/jpeg-compression-python.git
cd jpeg-compression-python
pip install -r requirements.txt
```

## How to Run

Open the notebook:

```bash
jupyter notebook jpeg_compression.ipynb
```

Then run the cells in order. The notebook uses a relative image path:

```python
image_path = Path("data/input/sample_image.png")
```

You can replace `sample_image.png` with another image as long as it is placed inside `data/input/`.

## Metrics

The project evaluates compression and reconstruction quality using:

- **Compression ratio**: ratio between original image size and compressed bitstream size.
- **Bits per pixel (BPP)**: number of compressed bits required per image pixel.
- **PSNR**: Peak Signal-to-Noise Ratio. Higher values indicate lower reconstruction error.
- **SSIM**: Structural Similarity Index. Values closer to 1 indicate higher structural similarity.

## Suggested Portfolio Description

**JPEG Compression Simulator in Python**  
Implemented a simplified JPEG compression and decompression pipeline using Python, including RGB-to-YCbCr conversion, 4:2:0 chroma subsampling, DCT, quantization, DPCM, zig-zag scanning, run-length encoding, Huffman coding, and image quality evaluation using PSNR and SSIM.

## Author

Vinícius Shinzato

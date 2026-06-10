# JPEG-like Image Compression and Digital Transmission Simulator

This project implements a simplified image compression and digital transmission pipeline in Python.

The first stage is based on a JPEG-like compression algorithm, including color space conversion, chroma subsampling, block-based DCT, quantization, zig-zag scanning, run-length encoding and Huffman coding.

The second stage simulates the digital transmission of image data over a noisy communication channel using BPSK modulation and an AWGN channel model.

The system performance is evaluated using compression ratio, Bit Error Rate (BER), Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM).

---

## Motivation

Digital images often require a large number of bits to be stored or transmitted. In bandwidth-limited communication systems, such as satellite links, drones, IoT cameras and remote sensing devices, image compression and robust transmission techniques are essential.

This project explores the trade-off between compression efficiency, channel noise, bit errors and reconstructed image quality.

---

## Features

- JPEG-like image compression
- RGB to YCbCr color space conversion
- Chroma subsampling
- 8x8 block processing
- Discrete Cosine Transform (DCT)
- Quantization
- Zig-zag scanning
- Run-Length Encoding (RLE)
- Huffman coding
- JPEG-like image reconstruction
- BPSK digital modulation
- AWGN channel simulation
- BPSK demodulation
- Image transmission from pixel bitstream
- BER, PSNR and SSIM analysis
- Automatic result saving

---

## Project Structure

```text
jpeg-compression-python/
├── data/
│   └── input/
├── results/
│   ├── images/
│   ├── plots/
│   └── tables/
├── jpeg_compression.ipynb
├── huffman.py
├── utils.py
├── README.md
├── requirements.txt
└── .gitignore

# # import anthropic

# # client = anthropic.Anthropic()

# # response = client.messages.create(
# #     model="claude-sonnet-4-20250514",
# #     max_tokens=256,
# #     messages=[{"role": "user", "content": "What is a neural network in one sentence?"}]
# # )

# # print(response.content[0].text)


# from datasets import load_dataset


# dataset = load_dataset("imdb", split="train")

# split = dataset.train_test_split(test_size=0.2, seed=42)
# train_val = split["train"].train_test_split(test_size=0.125, seed=42)

# train_ds = train_val["train"]
# val_ds = train_val["test"]
# test_ds = split["test"]

# print(f"Train: {len(train_ds)}, Val: {len(val_ds)}, Test: {len(test_ds)}")



# from huggingface_hub import hf_hub_download, snapshot_download

# model_path = hf_hub_download(
#     repo_id="sentence-transformers/all-MiniLM-L6-v2",
#     filename="config.json"
# )
# print(f"Cached at: {model_path}")

# model_dir = snapshot_download("sentence-transformers/all-MiniLM-L6-v2")
# print(f"Full model at: {model_dir}")



# from datasets import load_dataset

# # Load GLUE MRPC dataset
# dataset = load_dataset("glue", "mrpc")

# # Inspect first 5 examples from train split
# for i in range(5):
#     print(dataset["train"][i])
#     print("-" * 80)




# from datasets import load_dataset
# import time

# # Stream the C4 dataset
# dataset = load_dataset(
#     "allenai/c4",
#     "en",
#     split="train",
#     streaming=True
# )

# start_time = time.time()
# count = 0

# for example in dataset:
#     count += 1

#     # Stop after 10 seconds
#     if time.time() - start_time >= 10:
#         break

# elapsed = time.time() - start_time

# print(f"Processed {count} examples in {elapsed:.2f} seconds")
# print(f"Examples per second: {count / elapsed:.2f}")



# from datasets import load_dataset
# import pandas as pd
# import os

# # Load a small dataset
# dataset = load_dataset("imdb", split="train[:5000]")

# # Convert to pandas DataFrame
# df = dataset.to_pandas()

# # Save as CSV
# csv_file = "imdb_sample.csv"
# df.to_csv(csv_file, index=False)

# # Save as Parquet
# parquet_file = "imdb_sample.parquet"
# df.to_parquet(parquet_file, index=False)

# # Compare sizes
# csv_size = os.path.getsize(csv_file) / (1024 * 1024)
# parquet_size = os.path.getsize(parquet_file) / (1024 * 1024)

# print(f"CSV Size: {csv_size:.2f} MB")
# print(f"Parquet Size: {parquet_size:.2f} MB")



# from datasets import load_dataset

# # Load dataset
# dataset = load_dataset("imdb", split="train")

# # First split: 70% train, 30% temp
# split_1 = dataset.train_test_split(
#     test_size=0.30,
#     seed=42
# )

# train_dataset = split_1["train"]
# temp_dataset = split_1["test"]

# # Second split: split temp into 15% val and 15% test
# split_2 = temp_dataset.train_test_split(
#     test_size=0.50,
#     seed=42
# )

# val_dataset = split_2["train"]
# test_dataset = split_2["test"]

# # Verify sizes
# total = len(dataset)

# print(f"Total: {total}")
# print(f"Train: {len(train_dataset)} ({len(train_dataset)/total:.1%})")
# print(f"Validation: {len(val_dataset)} ({len(val_dataset)/total:.1%})")
# print(f"Test: {len(test_dataset)} ({len(test_dataset)/total:.1%})")


# import torch
# import torch.nn as nn


# def check_shapes(model, sample_input):
#     print(f"Input: {sample_input.shape}")
#     hooks = []

#     def make_hook(name):
#         def hook(module, inp, out):
#             in_shape = inp[0].shape if isinstance(inp, tuple) else inp.shape
#             out_shape = out.shape if hasattr(out, "shape") else type(out)
#             print(f"{name}: {in_shape} -> {out_shape}")
#         return hook

#     for name, module in model.named_modules():
#         if name:  # skip root module
#             hooks.append(module.register_forward_hook(make_hook(name)))

#     with torch.no_grad():
#         model(sample_input)

#     for h in hooks:
#         h.remove()


# # Simple CNN model
# model = nn.Sequential(
#     nn.Conv2d(3, 16, kernel_size=3, padding=1),
#     nn.ReLU(),
#     nn.MaxPool2d(2),

#     nn.Conv2d(16, 32, kernel_size=3, padding=1),
#     nn.ReLU(),
#     nn.MaxPool2d(2),

#     nn.Flatten(),

#     nn.Linear(32 * 56 * 56, 10)
# )

# # Fake image batch
# sample_input = torch.randn(8, 3, 224, 224)

# # Run shape debugger
# check_shapes(model, sample_input)





# import torch
# import torch.nn as nn
# import torch.optim as optim
# from torch.utils.tensorboard import SummaryWriter


# # Simple model
# model = nn.Sequential(
#     nn.Linear(10, 32),
#     nn.ReLU(),
#     nn.Linear(32, 1)
# )

# optimizer = optim.Adam(model.parameters(), lr=0.001)
# criterion = nn.MSELoss()

# # TensorBoard writer
# writer = SummaryWriter("runs/experiment_1")

# num_steps = 500

# for step in range(num_steps):

#     # Fake training data
#     x = torch.randn(16, 10)
#     y = torch.randn(16, 1)

#     # Forward
#     pred = model(x)
#     loss = criterion(pred, y)

#     # Backward
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

#     # Scalars
#     writer.add_scalar("loss/train", loss.item(), step)
#     writer.add_scalar("lr", optimizer.param_groups[0]["lr"], step)

#     # Histograms every 100 steps
#     if step % 100 == 0:
#         for name, param in model.named_parameters():
#             writer.add_histogram(f"weights/{name}", param, step)

#             if param.grad is not None:
#                 writer.add_histogram(f"grads/{name}", param.grad, step)

#     print(f"Step {step} | Loss: {loss.item():.4f}")

# writer.close()

# print("Training complete.")



# profile_train.py

# import torch
# import torch.nn as nn
# import torch.optim as optim

# model = nn.Sequential(
#     nn.Linear(784, 512),
#     nn.ReLU(),
#     nn.Linear(512, 10),
# )

# optimizer = optim.Adam(model.parameters(), lr=0.001)
# criterion = nn.CrossEntropyLoss()

# for step in range(200):
#     x = torch.randn(64, 784)
#     y = torch.randint(0, 10, (64,))

#     optimizer.zero_grad()

#     output = model(x)
#     loss = criterion(output, y)

#     loss.backward()
#     optimizer.step()

# print("Training complete")


# import tracemalloc
# from datasets import load_dataset

# def load_data():
#     dataset = load_dataset(
#         "ag_news",
#         split="train"
#     )

#     texts = dataset[:10000]["text"]

#     upper = (t.upper() for t in texts)

#     return upper


# # Start tracking memory allocations
# tracemalloc.start()

# # Run your pipeline
# data = load_data()

# # Take snapshot
# snapshot = tracemalloc.take_snapshot()

# # Get top memory-consuming lines
# top_stats = snapshot.statistics("lineno")

# print("\nTop 10 memory allocations:\n")

# for stat in top_stats[:10]:
#     print(stat)
#     for line in stat.traceback.format():
#         print(line)


# import torch
# import torch.nn as nn
# from torch.utils.data import TensorDataset, DataLoader
# from torch.utils.tensorboard import SummaryWriter

# # Fake dataset
# x_train = torch.randn(500, 20)
# y_train = (x_train.sum(dim=1) > 0).long()

# x_val = torch.randn(500, 20)
# y_val = (x_val.sum(dim=1) > 0).long()

# train_loader = DataLoader(
#     TensorDataset(x_train, y_train),
#     batch_size=32,
#     shuffle=True
# )

# val_loader = DataLoader(
#     TensorDataset(x_val, y_val),
#     batch_size=32
# )

# # Large model (easy to overfit)
# model = nn.Sequential(
#     nn.Linear(20, 256),
#     nn.ReLU(),
#     nn.Linear(256, 256),
#     nn.ReLU(),
#     nn.Linear(256, 2)
# )

# criterion = nn.CrossEntropyLoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# writer = SummaryWriter("runs/overfit_demo")

# epochs = 50

# for epoch in range(epochs):

#     # TRAIN
#     model.train()
#     train_loss = 0

#     for xb, yb in train_loader:
#         optimizer.zero_grad()

#         preds = model(xb)
#         loss = criterion(preds, yb)

#         loss.backward()
#         optimizer.step()

#         train_loss += loss.item()

#     train_loss /= len(train_loader)

#     # VALIDATION
#     model.eval()
#     val_loss = 0

#     with torch.no_grad():
#         for xb, yb in val_loader:
#             preds = model(xb)
#             loss = criterion(preds, yb)

#             val_loss += loss.item()

#     val_loss /= len(val_loader)

#     # LOGGING
#     writer.add_scalar("Loss/train", train_loss, epoch)
#     writer.add_scalar("Loss/validation", val_loss, epoch)

#     print(
#         f"Epoch {epoch:02d} | "
#         f"train_loss={train_loss:.4f} | "
#         f"val_loss={val_loss:.4f}"
#     )

# writer.close()


import torch
import torch.nn as nn

# Dummy model
model = nn.Sequential(
    nn.Linear(10, 32),
    nn.ReLU(),
    nn.Linear(32, 2)
)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

# Fake data
x = torch.randn(16, 10)
y = torch.randint(0, 2, (16,))

for step in range(5):

    optimizer.zero_grad()

    preds = model(x)

    loss = criterion(preds, y)

    loss.backward()

    # Pause execution here
    breakpoint()

    optimizer.step()

    print(f"step={step}, loss={loss.item():.4f}")
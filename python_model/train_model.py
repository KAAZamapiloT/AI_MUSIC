import torch
import torch.nn as nn

class MusicLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MusicLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x, _ = self.lstm(x)
        return self.fc(x)

# Define model
model = MusicLSTM(88, 128, 88)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loop with dummy data
for epoch in range(10):
    inputs = torch.randn(1, 100, 88)     # batch=1, seq=100, 88 notes
    targets = inputs                     # dummy target
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# Export to ONNX
dummy_input = torch.randn(1, 100, 88)
torch.onnx.export(model, dummy_input, "music_model.onnx", input_names=["input"], output_names=["output"])
print("✅ Exported trained model to music_model.onnx")

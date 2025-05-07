# python_model/train_model.py
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

model = MusicLSTM(88, 128, 88)
dummy_input = torch.randn(1, 100, 88)
torch.onnx.export(model, dummy_input, "music_model.onnx")

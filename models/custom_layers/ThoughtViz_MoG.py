import torch
import torch.nn as nn
import torch.nn.init as init

class MoG(nn.Module):
    def __init__(self, noise_dim):
        super(MoG, self).__init__()
        self.std = nn.Parameter(torch.empty(noise_dim))
        self.mean = nn.Parameter(torch.empty(noise_dim))
        self.initialize_parameters()

    def initialize_parameters(self):
        init.uniform_(self.std, a=-0.2, b=0.2)
        init.uniform_(self.mean, a=-1, b=1)

    def forward(self, noise):
        output = noise * self.std
        output += self.mean

        return output

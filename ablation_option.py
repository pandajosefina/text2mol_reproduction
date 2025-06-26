class AblationOption:
  def __init__(self, normalization_layer_removal, max_pool, hidden_layer_removal, conv_layer_removal, add_dropout):
    self.normalization_layer_removal = normalization_layer_removal
    self.max_pool = max_pool
    self.hidden_layer_removal = hidden_layer_removal
    self.conv_layer_removal = conv_layer_removal
    self.add_dropout = add_dropout

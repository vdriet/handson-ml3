is5 = [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1]
numberof5 = sum(is5)


def calc_precision(pos):
  assert 0 <= pos <= len(is5)
  numvalues = len(is5) - pos
  num5inset = sum(is5[pos:])
  precision = num5inset / numvalues
  return precision


def calc_recall(pos):
  assert 0 <= pos <= len(is5)
  num5inset = sum(is5[pos:])
  recall = num5inset / numberof5
  return recall


for i in range(len(is5)):
  precision = calc_precision(i)
  recall = calc_recall(i)
  print(f'position {i} precision {precision} recall {recall}')

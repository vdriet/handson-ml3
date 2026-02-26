def calc_mean(val1, val2):
  return (val1 + val2) / 2.0


def calc_f1(precision, recall):
  f1_score = 2 * precision * recall / (precision + recall)
  return f1_score


def print_calc(precision, recall):
  mean = calc_mean(precision, recall)
  f1 = calc_f1(precision, recall)
  print(f'For values precision {precision} and recall: {recall}')
  print(f'Regular mean: {mean:.4}\nHarmonic mean:{f1:.4}\nMinimum {min(precision, recall):.4}\n')


TP = 3
TN = 5
FP = 1
FN = 2
total_values = TP + TN + FP + FN
accuracy = (TP + TN) / total_values
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = calc_f1(precision, recall)
print(f"Accuracy:{accuracy:.4} Precision: {precision:.4} Recall: {recall:.4} F1 Score: {f1:.4}")

print_calc(0.5, 0.5)
print_calc(1.0, 0.0)
print_calc(0.2, 0.2)
print_calc(1.0, 0.2)

import math
import random


def calc_mae(y_hat, y):
    return abs(y_hat - y)


def calc_mse(y_hat, y):
    return (y_hat - y) ** 2


def regression_loss():
    num_samples = input(
        'Input number of samples (integer number) which are generated: ')
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return

    num_samples = int(num_samples)
    loss_name = input('Input loss name: ')
    final_loss = 0

    for i in range(num_samples):
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)

        if loss_name == 'MAE':
            loss = calc_mae(pred, target)
        else:
            loss = calc_mse(pred, target)

        print(
            f'loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}')
        final_loss += loss

    final_loss /= num_samples
    if loss_name == 'RMSE':
        final_loss = math.sqrt(final_loss)
    print(f'final {loss_name}: {final_loss}')


regression_loss()

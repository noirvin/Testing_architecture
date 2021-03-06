from pytest import raises


def get_average(li):
    if not isinstance(li, list):
        raise TypeError(
            f'This function takes a list of integers but got {type(li)} instead')
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return int(mean)


def test_get_average():
    nums = [5, 5, 10, 20]

    assert get_average(nums) == 10
    with raises(TypeError):
        get_average(2)

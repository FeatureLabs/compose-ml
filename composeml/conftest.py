import pandas as pd
import pytest

from composeml import LabelTimes
from composeml.tests.utils import read_csv


@pytest.fixture(scope="module")
def total_spent():
    data = [
        'id,customer_id,cutoff_time,total_spent',
        '0,0,2019-01-01 08:00:00,9',
        '1,0,2019-01-01 08:30:00,8',
        '2,1,2019-01-01 09:00:00,7',
        '3,1,2019-01-01 09:30:00,6',
        '4,1,2019-01-01 10:00:00,5',
        '5,2,2019-01-01 10:30:00,4',
        '6,2,2019-01-01 11:00:00,3',
        '7,2,2019-01-01 11:30:00,2',
        '8,2,2019-01-01 12:00:00,1',
        '9,3,2019-01-01 12:30:00,0',
    ]

    data = read_csv(data, index_col='id', parse_dates=['cutoff_time'])
    lt = LabelTimes(data=data, name='total_spent')
    lt.settings.update({'num_examples_per_instance': -1})
    return lt


@pytest.fixture(scope="module")
def labels():
    records = [
        {
            'label_id': 0,
            'customer_id': 1,
            'cutoff_time': '2014-01-01 00:45:00',
            'my_labeling_function': 226.92999999999998
        },
        {
            'label_id': 1,
            'customer_id': 1,
            'cutoff_time': '2014-01-01 00:48:00',
            'my_labeling_function': 47.95
        },
        {
            'label_id': 2,
            'customer_id': 2,
            'cutoff_time': '2014-01-01 00:01:00',
            'my_labeling_function': 283.46000000000004
        },
        {
            'label_id': 3,
            'customer_id': 2,
            'cutoff_time': '2014-01-01 00:04:00',
            'my_labeling_function': 31.54
        },
    ]

    dtype = {'cutoff_time': 'datetime64[ns]'}
    values = pd.DataFrame(records).astype(dtype).set_index('label_id')
    values = values[['customer_id', 'cutoff_time', 'my_labeling_function']]
    values = LabelTimes(values, name='my_labeling_function', target_entity='customer_id')
    return values


@pytest.fixture(autouse=True)
def add_labels(doctest_namespace, labels):
    doctest_namespace['labels'] = labels

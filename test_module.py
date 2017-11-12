# test_module.py

# call the method in another file

from unittest import mock

import module

@mock.patch('module.ClassIWantToMock')
def main(mock_module):
    real = module.ClassIWantToMock()

    print (real.method_to_mock(2))

if __name__ == '__main__':
    main()

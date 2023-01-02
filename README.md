# python-snippets
Some useful snippets in python

## [ping()](https://github.com/odoo-app-dev/python-snippets/blob/main/ping.py)
   record a logging warning in case of reachable or unreachable results.
   Note: it needed some works to be more useful
   
## [ping_test()](https://github.com/odoo-app-dev/python-snippets/blob/main/ping_test.py)
platform detection; windows or linux

   `ping_test('amazon.com') -> 'amazon.com,172,ms'`
   
  `ping_test() -> '8.8.8.8,41,ms'`
   
   `ping_test('172.16.0.1') -> False`

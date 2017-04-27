from setuptools import setup, find_packages

setup(
    name='kafka-logger',
    packages=find_packages(exclude=['build', 'docs', 'templates']),
    version='0.3.0',
    description='A simple Kafka logger in Python.',
    author='Peijie Hu',
    author_email='peijie@peijiehu.com',
    license='MIT',
    url='https://github.com/peijiehu/kafka-logger',
    keywords=['python', 'kafka', 'logstash', 'logging'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
)

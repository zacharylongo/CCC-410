![Local Image](images/Firewatch.png)


Welcome to FireWatch , a collection of modules for host enumeration, document analysis/retrival, and more.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Modules](#modules)
   - [FireWatch Module](#firewatch-module)
   - [Intel-Xtinguisher Module](#intel-xtinguisher-module)
   - [Shodan Module](#shodan-module)
5. [Service Selector](#service-selector)
6. [Creator](#creator)

## Introduction<a name="introduction"></a>

The FireWatch Suite provides a set of tools for conducting various types of analysis on domains and hosts. From domain registration checks to document analysis, this suite offers a comprehensive solution for information gathering.

## Installation<a name="installation"></a>

To install the FireWatch Suite, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/zacharylongo/CCC-410.git
   ```

2. Navigate to the directory:
   ```bash
   cd CCC-410/FireWatch
   ```

3. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage<a name="usage"></a>

To use the FireWatch Suite, execute the `Service_selector.py` file and follow the on-screen instructions to select a service. Alternatively, you can run individual modules directly.

```bash
python Service_selector.py
```

## Modules<a name="modules"></a>

### FireWatch Module<a name="firewatch-module"></a>

The FireWatch Module, also known as Firewatch.py, is a tool for host enumeration and data analysis. It provides functionalities such as domain registration checks, domain IP lookup, reverse IP lookup, DNS record retrieval, WHOIS information retrieval, certificate (CERT) information retrieval, domain reputation check, subdomain scanning, and historical WHOIS data retrieval.

### Intel-Xtinguisher Module<a name="intel-xtinguisher-module"></a>

The Intel-Xtinguisher Module, also known as `intelx_scan.py`, focuses on document analysis and enumeration. It provides features for searching and analyzing documents using the intelx.io platform.

### Shodan Module<a name="shodan-module"></a>

The Shodan Module, also known as `shodan_scan2.py`, offers a less powerful alternative to the FireWatch Module. It provides functionalities for conducting host enumeration and data analysis using the Shodan platform.

## Service Selector<a name="service-selector"></a>

The `Service_selector.py` file serves as a main menu for accessing different modules within the FireWatch Suite. It allows users to select a service from a list of available options.

## Creator<a name="creator"></a>

The FireWatch Suite was created by Zachary Longo.

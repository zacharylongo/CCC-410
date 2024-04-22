<img width="900" alt="Firewatch " src="https://github.com/zacharylongo/CCC-410/assets/71234688/0a2fb711-9bfb-4186-9416-cc0cf5e14ff1">

## Table of Contents 🔥

1. [Introduction](#introduction) 
2. [Installation](#installation) 
3. [Usage](#usage) 
4. [Modules](#modules) 
   - [FireWatch Module](#firewatch-module) 
   - [Intel-Xtinguisher Module](#intel-xtinguisher-module) 
   - [Shodan Module](#shodan-module) 
5. [Service Selector](#service-selector) 
6. [Creator](#creator) 

## Introduction<a name="introduction"></a> ✍️

The FireWatch Suite provides a set of simple API tools for conducting various types of OSINT analysis on domains and hosts. From domain registration checks to document identification, this suite offers a near comprehensive solution for information gathering.

The suite relies on Several API's:

💲 = Partial Functionality without paid subscription

⚠️ = Free, but limited tokens without paid subscription

👍 = 100% Free To use 

* Intelx.io 💲⚠️
* HackerTarget.io 💲⚠️
* Shodan.io 💲⚠️
* WhoIsXML.io ⚠️
* WhoIsFreaks 👍

## Installation<a name="installation"></a> 🔨

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
4. Configure API Keys
   * Firewatch.py is 100% functional without any paid subscriptions. However, you **MUST** register for a WhoisXML **AND** WhoIsFreaks account for full functionality.
   * These keys can simply be pasted into ``` config.json ``` with no further configuration required. 

## Usage<a name="usage"></a> 🛠️

To best utilize the FireWatch Suite, execute the `Service_selector.py` file and follow the on-screen instructions to select a service. Alternatively, you can run individual modules directly if that's what you desire.

```bash
python Service_selector.py
```

## Modules<a name="modules"></a> ⚙️

### FireWatch Module<a name="firewatch-module"></a> 🔥

The FireWatch Module, also known as Firewatch.py, is a tool for host enumeration and data analysis. It provides functionalities such as domain registration checks, domain IP lookup, reverse IP lookup, DNS record retrieval, WHOIS information retrieval, certificate (CERT) information retrieval, domain reputation check, subdomain scanning, and historical WHOIS data retrieval.

### Intel-Xtinguisher Module<a name="intel-xtinguisher-module"></a> 🧯

The Intel-Xtinguisher Module, also known as `intelx_scan.py`, focuses on document analysis and enumeration. It provides features for searching and analyzing documents using the intelx.io platform.

### Shodan Module<a name="shodan-module"></a> 🚧

The Shodan Module, also known as `shodan_scan2.py`, offers a less powerful alternative to the FireWatch Module. It provides functionalities for conducting host enumeration and data analysis using the Shodan platform.

## Service Selector<a name="service-selector"></a> ☝️

The `Service_selector.py` file serves as a main menu for accessing different modules within the FireWatch Suite. It allows users to select a service from a list of available options.

## Creator<a name="creator"></a>

The FireWatch Suite was created by Zachary Longo.

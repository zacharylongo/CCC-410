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

The FireWatch Suite provides a set of simple API tools for conducting various types of OSINT analysis on domains and hosts. From domain registration checks to document identification, this suite offers a near comprehensive solution for public facing domain information gathering.

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
   * These keys will be requested when you first boot up FireWatch. Alternatively, you can simply paste them into config.json **(Not to be confused with default_config.json)**

## Usage<a name="usage"></a> 🛠️

To best utilize the FireWatch Suite, execute the `Service_selector.py` file and follow the on-screen instructions to select a service. Alternatively, you can run individual modules directly if that's what you desire.

```bash
python Service_selector.py
```

## Modules<a name="modules"></a> ⚙️

### FireWatch Module<a name="firewatch-module"></a> 🔥

The FireWatch Module, also known as Firewatch.py, is a tool for host enumeration and data analysis. It provides functionalities such as domain registration checks, domain IP lookup, reverse IP lookup, DNS record retrieval, WHOIS information retrieval, certificate (CERT) information retrieval, domain reputation check, subdomain scanning, and historical WHOIS data retrieval. This tool combines all of these metrics into easily readable terminal outputs.

### Intel-Xtinguisher Module<a name="intel-xtinguisher-module"></a> 🧯

The Intel-Xtinguisher Module, also known as `intelx_scan.py`, focuses on document analysis and enumeration. It provides features for searching and analyzing files/documents using the intelx.io platform. It additionally offers advanced parameters that are further detailed in Intelx.io's API documentation.

 * This module also exports results to an easily readable .csv file! 😃

### Shodan Module<a name="shodan-module"></a> 🚧

The (Unfinished) Shodan Module, also known as `shodan_scan2.py`, offers an (albeit less powerful) alternative to the FireWatch Module. It provides functionalities for conducting host enumeration and data analysis using the Shodan platform as a second source of info.
 
* When finished, this module will focus on ennumerating Industrial Control Systems (ICS) related to Smart Buildimg and manufacturing reconaissance efforts. In it's current state, it is rather redundant; however this will change soon.

## Service Selector<a name="service-selector"></a> ☝️

The `Service_selector.py` file serves as a main menu for accessing different modules within the FireWatch Suite. It allows users to select a service from a list of available options. It isn't necessary to utilize, however it may keep things more organized in the event you'd like to process multiple requests.

## Creator/Remarks<a name="creator"></a>

The FireWatch Suite and its modules were created by I (Zachary Longo) utilizing a mixture between official API Documentation, forum posts, and aid from ChatGPT/Github Co-Pilot. All sources are linked in the sources tab contained within this repositories wiki.

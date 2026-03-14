# SoK: After Decades of Web Tracker Detection, What’s Next?

# --> Will be made available on ZENODO after review.  

## Abstract
Web tracking is an omnipresent phenomenon in today's web, affecting users in their day-to-day lives. Filter lists and blockers were invented to detect trackers and to protect users. Due to limitations of said tools, researchers developed web tracker detectors to replace them. 
No review constructed a universal perspective and classification of web tracker detectors until now. Past reviews focused either on the field as a whole or on web tracking techniques. In this SoK paper, we present the most comprehensive study on web tracker detection by systematizing and synthesizing the available knowledge. We conduct a systematic review, resulting in 59 primary and 16 supplementary studies out of a corpus of 832 papers. Based on these findings we suggest a taxonomy, observe and evaluate trends, propose open research gaps, and recommendations with which we aim to lay the foundations for future web tracker detection research. In addition, we conduct a limited reproducibility study to assess the validity of past studies and highlight emerging problems in this field.

## Repository Structure

The repository is organized to mirror the methodological workflow of the SoK paper. 
At a high level, the repository contains directories and files corresponding to the 
major phases of our methodology. These materials may include the study corpus, screening 
and eligibility records, data extraction sheets, coding and classification resources, 
taxonomy artifacts, figures, and supplementary notes. Together, they 
document how the evidence base was constructed. 

#### Excel Processor
After exporting all the results from the digital libraries to excel sheets, we
run a simple deduplication script to remove duplicated entries. 

#### Figures
Here are all the final figures used in our SoK paper. 

#### List of artifacts
Here is an excel sheet that contains links to the available artifacts of the 
primary studies that have been examined in the SoK paper. 

#### Lit Review Results
This directory is structured according to the phases of our methodology (see 
image in figures folder, SoK Review Figure).

- **lit_review_results/1-identification_phase** contains the raw data, i.e., the exports
from the digital libraries and the compiled review_reports that were then used by
the reviewers.

- **lit_review_results/2-screening_phase** contains the excel sheets from both
reviewer A and B and a summary of their decisions and the final decision. 

#### PETS paper crawler
A simple crawler can be found here, one for results from 2025 and one for before. 
In addition, a script to execute the pre-defined search string. 

## Security/Privacy Issues and Ethical Concerns 
This artifact accompanies our SoK paper and primarily consists of documentation 
and analysis materials. The artifact does not contain exploits, malware samples, 
vulnerable software, or code that disables or modifies security mechanisms on the
evaluator’s system. As such, evaluating or inspecting the artifact does not 
require elevated privileges, modification of operating system protections, 
or interaction with potentially harmful binaries.

From a privacy perspective, the artifact does not contain personal data, user 
tracking data, or datasets derived from human subjects. The materials are based 
exclusively on publicly available academic publications and publicly accessible 
documentation of web tracking detection techniques. Consequently, no identifiable 
information about individuals is collected, processed, or distributed as part of 
this artifact.

All in all, we are not aware of any security, privacy, or ethical risks associated with 
inspecting or reusing the materials provided in this artifact beyond the standard 
considerations involved in handling research data and documentation. 

## Installation Guide

To replicate the environment and set up the necessary tools for this project,
follow the step-by-step instructions outlined below:

1. Ensure that Python 3.10.11 is installed on your system (this was the used
   Python version, other version might work as well). If you do not have
   Python 3.10.11, download and install it
   from the official [Python website](https://www.python.org/downloads/),
   [asdf](https://asdf-vm.com), or another tool of your choice.


2. **(Optional:)** Install
   the [Conda](https://docs.conda.io/en/latest/miniconda.html) package
   manager, which can be utilized for
   managing dependencies and creating a virtual environment or use your IDE (
   e.g. PyCharm for venv) and PIP.

3. Clone the GitHub repository to your local machine (HTTP/S):
   ```
   git clone https://github.com/wolfrieder/sok_artifact_web_tracker_detection.git
   ```


4. Navigate to the cloned repository's root directory:
   ```
   cd sok_artifact_web_tracker_detection
   ```
   
5. Create a new virtual environment with Python 3.10.11. Either through your IDE
   or use the following command (which creates a virtual environment and
   installs the packages from the `requirements.txt`:

   ```
   sh init.sh
   ```

6. OPTIONAL: Install the necessary packages from the `requirements.txt` file:
   ```
   pip install -r requirements.txt
   ```

With these steps completed, you should now have a functional environment. 

## Search Term Matrices
### ACM Digital Library
The following search resulted in 498 papers that were then filtered for research 
articles (n=105) and short papers (n=7). The search matrix is reported in 
Section 4 Research Methodology. 
```
[Publication Title: web track* OR "ad blocker" OR first*party* track* OR 
third*party* track*] OR [Abstract: "web tracker" OR "web tracking" OR "ad tracker" 
OR "ad blocking" OR first*party* track* OR third*party* track* OR "browser fingerprinting" 
OR "web tracker detection"] OR [[[Keywords: "web tracker detection" OR "web tracker" 
OR "web tracking" OR "web privacy" OR "web privacy measurement"]] AND 
[[NOT [Publication Title: eye* OR blockchain]]]
```

### IEEE Xplore 
This search resulted in 303 papers, with conference papers (n=283) and
journal articles (n=20). The IEEE Xplore search interface did not allow us to use 
more than ten wildcard characters in one search, which is why we had to use it selectively.

```
("Document Title":Web Track*) OR ("Document Title":"Ad Blocker" OR "Document 
Title":First*Party Track* OR "Document Title":Third*Party Track*) NOT ("Document 
Title":eye* OR "Document Title":Blockchain OR "Document Title":eye-tracking) OR 
("Abstract":"Web tracker OR "Abstract":"Web Tracking" OR "Abstract":"Ad tracker 
OR "Abstract":"Ad Blocking" OR "Abstract":First*Party Track* OR "Abstract":Third*Party 
Track* OR "Abstract":"Browser Fingerprinting" OR "Abstract":"Web Tracker Detection") 
OR ("Author Keywords":"Web Tracker Detection" OR "Author Keywords":"Web tracker OR 
"Author Keywords":"Web Tracking" OR "Author Keywords":"Web Privacy" OR "Author 
Keywords":"Web Privacy Measurement")
```

### Scopus 
Compared to other digital libraries, we can see the applied filters within the 
search matrix. Furthermore, we set the subject area to computer science to 
reduce the number of results, resulting in conference papers (n=160) and articles (n=57). 

```text
( TITLE ( web AND track* OR "ad blocker" OR first*party AND track* OR third*party 
AND track* AND not AND eye* AND not AND blockchain AND not "Data Leaks" ) OR ABS 
( "web tracker" OR "web tracking" OR "ad tracker" OR "ad blocking" OR first*party 
AND track* OR third*party AND track* OR "browser fingerprinting" OR "web tracker detection" 
not AND eye* AND not AND blockchain AND not "Data Leaks" ) OR KEY ( "web tracker detection" 
OR "web tracker" OR "web tracking" OR "web privacy" OR "web privacy measurement" ) ) 
AND PUBYEAR > 1995 AND PUBYEAR < 2025 AND PUBYEAR > 1998 AND PUBYEAR < 2025 AND 
( LIMIT-TO ( SUBJAREA , "COMP" ) ) AND ( LIMIT-TO ( DOCTYPE , "cp" ) OR LIMIT-TO ( DOCTYPE , "ar" ) ) 
AND ( LIMIT-TO ( LANGUAGE , "English" ) ) 
```

### Springer Link
The Springer Link interface did not offer the same possibilities as other digital 
libraries. We had to enter each word individually in the same order as shown below. 
In addition, the exported file did not contain all relevant information, which 
required manual effort to add the missing information for the review template. 
Only conference papers (n=98) were exported. 

```text
(Web track* OR Web tracker detection OR Browser Fingerprinting OR First*Party Track* 
OR Third*Party Track* OR Web Privacy) AND NOT (eye*, blockchain) 
```

### USENIX
This conference offers their own search interface, albeit limited in its 
functionality. Results were manually exported and missing information such as URLs 
and DOIs added. Note that published papers do not have keywords. 

```text
"web tracking" OR "web tracker OR "ad tracker OR "ad blocking" OR 
"browser fingerprinting" OR "web tracker detection" OR "web tracking detection" 
```

### PETS
There was no search interface for PETS, which is why we wrote two crawlers 
to extract all papers from the proceedings webpage -- one for old volumes 
and one for the newest volume of 2025 as they had a different format than the 
older volumes at the time of crawling (November 5). 
In addition, volumes before 2015 were not addressed by the crawler as older 
proceedings were published by Springer International, thus available through 
the Springer Link interface. 

```text
Title ("web track.*", "ad blocker", "first.*party.*track.*",
    "third.*party.*track.*") OR Abstract ("web tracker, "web tracking", "ad tracker, "ad blocking",
    "first.*party.*track.*", "third.*party.*track.*",
    "browser fingerprinting",
    "web tracker detection") OR Keywords ("web tracker detection", "web tracker, "web tracking",
    "web privacy", "web privacy measurement") AND NOT ("eye.*", "blockchain")
```

## Reference

```text
@INPROCEEDINGS {sok-tracker-detection,
author = { Rieder, Wolf and Raschke, Philip and Cory, Thomas and Sechting, Christian René
 and Kumar, Aditya and Küpper, Axel},
booktitle = { 2026 IEEE Symposium on Security and Privacy (SP) },
title = {{ SoK: After Decades of Web Tracker Detection, What’s Next?}},
year = {2026},
volume = {},
ISSN = {},
pages = {},
doi = {},
url = {},
publisher = {IEEE Computer Society},
address = {Los Alamitos, CA, USA},
}
```
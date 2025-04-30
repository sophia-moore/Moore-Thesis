### Given a scenario, date, and question, determine which section  of the Internal Revenue Code is applicable and generate a conclusion.
---

**Source**: <https://nlp.jhu.edu/law/>

**Size (samples)**: 69

**Legal reasoning type**: Interpretation

**Task type**: Classification, Conclusion

## Task description

The StAtutory Reasoning Assessment (SARA) dataset investigates the effects of natural language
understanding approaches on statutory reasoning. SARA includes a set of Internal Revenue Code (IRC) statutes, cases, and prompts. A subset of SARA relates to entailment, and asks questions about specific sections of the SARA statutes. 

We modify these SARA entailment tasks to determine whether models can effectively recall, apply, and make conclusions using legal rules. This represents a test of the legal Issue-spotting (I), rule-Recall (R), rule-Application (A) and rule-Conclusion (C) framework (IRAC). 

## Task construction

For detailed information surrounding construction of the SARA dataset, refer to the [SARA](https://ceur-ws.org/Vol-2645/paper5.pdf) or [LegalBench](https://arxiv.org/pdf/2308.11462) papers. These tasks and prompts draw specifically from the public-access [SARA](https://github.com/SgfdDttt/sara) and [LegalBench](https://github.com/HazyResearch/legalbench) repositories. For information surrounding the construction of this modified subset, refer to the accompanying paper.

Note: The original SARA dataset contains both entailment prompts and numerical questions which require computing the amount of tax owed. This subset only contains modified entailment tasks.

## Citation information
If you use this modified dataset, we ask that you also cite the original source:

bib
@article{holzenberger2021factoring,
  title={Factoring statutory reasoning as language understanding challenges},
  author={Holzenberger, Nils and Van Durme, Benjamin},
  journal={arXiv preprint arXiv:2105.07903},
  year={2021}
}


## Data column names

- **Description**:  A given case description related to US federal tax law. 
- **Question**: The question to answer based on the given description. 
- **Text**:  The concatenation of the description and question. This is intended as the input to the model, adhering to the LegalBench format. Should the text exceed the context window of the model, it is recommended to truncate from the left. 
- **Section**: The applicable section of the Internal Revenue Code (IRC). 
- **Answer**: The answer to the question. Answers to questions are dollar amounts or true/false ("yes" or "no").

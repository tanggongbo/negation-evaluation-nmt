This repository provides the manual evaluation results and the contrastive test sets on negation in the paper [Revisiting Negation in Neural Machine Translation (to appear)].

The manual evaluations are conducted on 4 language directions, Chinese-English, English-Chinese, German-English, and English-German. The Chinese-English test sets are from [NegPar](https://github.com/qianchu/NegPar), and the test sets on German-English are randomly selected from [LingEval97](https://github.com/rsennrich/lingeval97). 

Following [LingEval97](https://github.com/rsennrich/lingeval97), we also create a contrastive test set for negation on Chinese-English, considering both negation addition and deletion. The negation deletion and negation addition categories have 2,005 and 3,062 instances with contrastive translations, respectively. 


If you use the data or refer the evaluation results, please cite this paper:

    @article{tang-etal-2021-revisiting,
    title = "Revisiting Negation in Neural Machine Translation",
    author = "Tang, Gongbo  and
      R\"onchen, Philipp  and
      Sennrich, Rico  and
      Nivre, Joakim",
    journal = "Transactions of the Association for Computational Linguistics",
    year = "2021"
    }


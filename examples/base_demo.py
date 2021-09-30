# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys

sys.path.append('..')
from pytextclassifier import TextClassifier

if __name__ == '__main__':
    m = TextClassifier(model_name='textcnn')
    # model_name is choose classifier, support lr, random_forest, xgboost, svm, mlp, ensemble, stack
    print(m)
    data = [
        ('education', 'Student debt to cost Britain billions within decades'),
        ('education', 'Chinese education for TV experiment'),
        ('sports', 'Middle East and Asia boost investment in top level sports'),
        ('sports', 'Summit Series look launches HBO Canada sports doc series: Mudhar')
    ]
    m.train(data)

    r = m.predict(['Abbott government spends $8 million on higher education media blitz',
                   'Middle East and Asia boost investment in top level sports'])
    print(r)
    m.save()
    del m

    new_m = TextClassifier()
    new_m.load()
    predict_label_prob = new_m.predict_proba(['Abbott government spends $8 million on higher education media blitz'])
    print(predict_label_prob)  # [[0.53337174 0.46662826]]
    print('classes_: ', new_m.model.classes_)  # the classes ordered as prob

    predict_label = new_m.predict(['Abbott government spends $8 million on higher education media blitz',
                                   'Middle East and Asia boost investment in top level sports'])
    print(predict_label)  # ['education', 'sports']

    test_data = [
        ('education', 'Abbott government spends $8 million on higher education media blitz'),
        ('sports', 'Middle East and Asia boost investment in top level sports'),
    ]
    acc_score = new_m.evaluate(test_data)
    print(acc_score)  # 1.0

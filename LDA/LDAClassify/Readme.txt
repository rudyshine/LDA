��������: ����sklearn�Դ���20 newsgroups (~20000ƪ�ĵ�)��nltk�Դ���reuters(10788ƪ�ĵ�)

ldaExp.py: ��gensim��ָ������(20newsgroup ����reuters��ͨ��������ָ������֮һ)��ѧϰdoc-topic�ֲ�������Ϊ '������-train-�ĵ���.svm-lda.txt' �� '������-test-�ĵ���.svm-lda.txt'

classEval.py: ��ldaExp.py���ɵ� '������-train-�ĵ���.svm-lda.txt' ��Ϊ�����ļ�������ѵ������ '������-test-�ĵ���.svm-lda.txt' �ϲ��Է���Ч����

corpusLoader.py: ��sklearn��20newsgroups��nltk��reutersͳһ�����Ϸ��ʽӿڡ�

��������ʵ��:
- python ldaExp.py 20news
���� '20news-train-11314.svm-lda.txt' �� '20news-test-7532.svm-lda.txt'
- python classEval.py 20news lda
ѵ��������ģ��Ч��

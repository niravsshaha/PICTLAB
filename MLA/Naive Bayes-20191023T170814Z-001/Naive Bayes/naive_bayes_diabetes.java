package naive_bayes_classifier;

import java.io.BufferedReader;
import java.io.FileReader;
import java.lang.Exception;

import weka.core.Instances;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.Evaluation;

//build path->configure build path->add ext jar
public class naive_bayes {
	
	naive_bayes()
	{
		try
		{
			BufferedReader training_buffer= new BufferedReader(new FileReader("C:\\Users\\RAMANI\\Desktop\\CL-VII\\naive_bayes\\diabetes_arff.arff"));
			BufferedReader testing_buffer= new BufferedReader(new FileReader("C:\\Users\\RAMANI\\Desktop\\CL-VII\\naive_bayes\\diabetes_arff.arff"));
					
			Instances train=new Instances(training_buffer);
			Instances test=new Instances(testing_buffer);
			
			train.setClassIndex(train.numAttributes()-1);
			test.setClassIndex(test.numAttributes()-1);
			
			NaiveBayes model=new NaiveBayes();
			model.buildClassifier(train);
			
			Evaluation result_set=new Evaluation(test);
			result_set.evaluateModel(model, test);
			
			System.out.printf("Accuracy of model= %.3f\n",result_set.pctCorrect());
			System.out.printf("Error rate= %.3f\n",result_set.errorRate()*100);
			
			for(int i=0;i<test.numClasses();i++)
			{
				System.out.println("\n\n******FOR CLASS "+(i+1)+"***********");
				System.out.printf("Precision is %.3f\n",result_set.precision(i));
				System.out.printf("Recall is %.3f\n",result_set.recall(i));
				System.out.printf("FPR is %.3f\n",result_set.falsePositiveRate(i));
				System.out.printf("FNR is %.3f\n",result_set.falseNegativeRate(i));
				System.out.printf("TNR is %.3f\n",result_set.trueNegativeRate(i));
			}
			
		}
		catch(Exception e)
		{
			System.err.println("Error encountered");
		}
	}
	public static void main(String args[])
	{
		naive_bayes NaiveBayes=new naive_bayes();
	}

}

ppi
===

Protein-Protein Interactions

Dependencies
------------
matplotlib
networkx
colorama

main.py options
---------------
    To see main.py options run 'python main.py -h'

    ====================================================================================
      % python main.py -h
      %
      % usage: main.py [-h] [-v] [-k KFOLDCROSS] [-s SAMPLESIZE] [-t]
      % 
      % optional arguments:
      %   -h, --help            show this help message and exit
      %   -v, --verbose         Increases verbosity.
      %   -k KFOLDCROSS, --kfoldcross KFOLDCROSS
      %                         Cross validates k times
      %   -s SAMPLESIZE, --samplesize SAMPLESIZE
      %                         Percentage of test1 to train on. Example: -s 0.9 will
      %                         use 90 percent of test1 to train on.
      %   -t, --test2           Run predictions on trainingset Test2.txt.
    ====================================================================================

How to cross-validate
---------------------
    Example 1 (cross-validate 3 times, samplesize 80%):
        ====================================================================================
        % python main.py -k 3 -s 0.8    
        % Namespace(kfoldcross=3, samplesize=0.8, test2=False, verbose=False)
        % 
        % Confusion Matrix 
        % 
        %   Tp  |  Fn        12   |  13  
        % -------------    ------------------
        %   Fp  |  Tn        26   |  150  
        % 
        % Precision: 0.315789  Recall: 0.480000  F-Measure: 0.380952
        % 
        % Confusion Matrix 
        % 
        %   Tp  |  Fn        7    |  16  
        % -------------    ------------------
        %   Fp  |  Tn        34   |  144  
        % 
        % Precision: 0.170732  Recall: 0.304348  F-Measure: 0.218750
        % 
        % Confusion Matrix 
        % 
        %   Tp  |  Fn        8    |  13  
        % -------------    ------------------
        %   Fp  |  Tn        24   |  156  
        % 
        % Precision: 0.250000  Recall: 0.380952  F-Measure: 0.301887
        % 
        % 
        % Average F-Measure: 0.300529724468
        % Hit Enter to continue... 
        ====================================================================================


import os 
os.environ['TOKENIZERS_PARALLELISM']="false"
from TextSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from TextSummarizer.entity import DataTransformationConfig
from pathlib import Path



# class DataTransformation:
#     def __init__(self,config: DataTransformationConfig):
#             self.config= config
#             logger.info("Assigning Tokenizer")
#             try:
#                 self.tokenizer=AutoTokenizer.from_pretrained(config.tokenizer_name,)
#                                                              # local_files_only=True)
#                 #self.tokenizer=AutoTokenizer.from_pretrained("this-tokenizer-does-not-exist-123", local_files_only=True )
#             except Exception as e:
#                 logger.info("Assigning Tokenizer Failed")
#                 raise 
#             logger.info("Assigning Tokenizer Done")


#     def convert_examples_to_features(self,example_batch):
#         input_encodings=self.tokenizer(example_batch['dialogue'],max_length=1024,truncation=True) #dialogue

#         with self.tokenizer.as_target_tokenizer():
#             target_encodings= self.tokenizer(example_batch['summary'],max_length=1024,truncation=True)

#         return {
#             'input_ids': input_encodings['input_ids'],
#             'attention_mask': input_encodings['attention_mask'],
#             'labels':target_encodings['input_ids']
#         }
    

#     def create_dirs_files(self):
#         dirs=""
#         l=str(self.config.data_path).split('/')[2:]
#         for i in l:
#              dirs+='/'+i
          
#         dataset_loc=Path(self.config.data_path).resolve()  #
#         desired_location=Path(self.config.root_dir).resolve()
#         desired_location=desired_location.joinpath(dirs).resolve()
#         desired_location.mkdir( parents=True, exist_ok=True)
        
#         for root,d,files in os.walk(dataset_loc):
#             rel_path = Path(root).relative_to(dataset_loc)           
#             target_dir = desired_location / rel_path
            
#             target_dir.mkdir(parents=True,exist_ok=True)

#             for file in files:
#                 empty_file = target_dir / file
#                 empty_file.touch(exist_ok=True)


#     def convert(self):
#         logger.info("Starting Convert")
#         dataset_path = Path(self.config.data_path)
        
#         dataset_samsum = load_from_disk(f"file://{dataset_path}")
#         logger.info("Loaded from disk")
#         # print(dataset_samsum.column_names)
#         logger.info("Starting map")
#         dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
#         logger.info("done mapping")
        
#         save_dir = Path(self.config.root_dir).joinpath("DataSet/samsum_dataset").resolve()
        
#         logger.info("Creating dirs")
#         self.create_dirs_files()
#         logger.info("Created dirs")
        
#         dataset_samsum_pt.save_to_disk(save_dir)
#         logger.info("Saved to disk")


class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config= config
        logger.info("Assigning Tokenizer")
        try:
            self.tokenizer=AutoTokenizer.from_pretrained(config.tokenizer_name,use_fast=False,
                                                            local_files_only=True
                                                            )
            self.tokenizer.encode("warmup")
            #self.tokenizer=AutoTokenizer.from_pretrained("this-tokenizer-does-not-exist-123", local_files_only=True )
        except Exception as e:
            logger.exception("Assigning Tokenizer Failed")
            raise 
        logger.info("Assigning Tokenizer Done")


    def convert_examples_to_features(self,example_batch):
        input_encodings=self.tokenizer(example_batch['dialogue'],max_length=1024,truncation=True) #dialogue

        with self.tokenizer.as_target_tokenizer():
            target_encodings= self.tokenizer(example_batch['summary'],max_length=1024,truncation=True)

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels':target_encodings['input_ids']
        }
    

    def create_dirs_files(self):
        dirs=""
        l=str(self.config.data_path).split('/')[2:]
        for i in l:
             dirs+=i+'/'
          
        dataset_loc=Path(self.config.data_path).resolve()  #
        desired_location=Path(self.config.root_dir).resolve()
        desired_location=desired_location.joinpath(dirs)
        os.makedirs(desired_location,exist_ok=True)

        for root,d,files in os.walk(dataset_loc):
            rel_path = Path(root).relative_to(dataset_loc)           
            target_dir = desired_location / rel_path
            
            target_dir.mkdir(parents=True,exist_ok=True)

            for file in files:
                empty_file = target_dir / file
                empty_file.touch(exist_ok=True)


    def convert(self):
        dataset_path = Path(self.config.data_path)
        
        dataset_samsum = load_from_disk(f"file://{dataset_path}")
        print(dataset_samsum.column_names)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
        
        save_dir = Path(self.config.root_dir).joinpath("DataSet/samsum_dataset")
        
        self.create_dirs_files()
        
        dataset_samsum_pt.save_to_disk(str(save_dir))








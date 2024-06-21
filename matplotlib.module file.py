import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('student_data.log')

# Set log level for handlers
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.INFO)

# Create formatters and add them to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logging.info("creating plot bar graph")
party=['ycp','tdp','jsn','bjp','congress']
votes=[100,120,110,90,80]
plt.bar(party,votes,color=['blue','yellow','red','orange','green'])
plt.xlabel("party")
plt.ylabel("votes")
plt.title("election votes")
plt.show()
logging.info("plot bar graph successfully crated")

# ssc_std=['boys','girls','pass','fail']
# ssc_results=[80,40,90,30]
# plt.bar(ssc_std,ssc_results,color=['red','blue','green','yellow'])
# plt.xlabel("ssc_std")
# plt.ylabel("ssc_result")
# plt.title("ssc_marks_result")
# plt.show()
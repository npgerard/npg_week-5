import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write(
'''
# Titanic Visualization 1

'''
)
# Generate and display the figure
st.write("Is the 'women and children first' sentiment evident in survivor statistics?")
fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)

st.write(
 """
With regard to family size and last name analyis - no, the two datasets returned by the functions family_groups() and last_names() do not agree.
\n
Results of family_group()) shows there are family groups of sizes 8 and 11.
Results of last_names() shows there is no grouping of family last name with the counts of 8 or 11
\n
Furthermore, there is a last name, 'Anderson' with a count of 9.  There are no family group sizes of 9
\n
This is unsurprising, as it is invalid to assume any two passengers with the last name are part of the same family, particularly without regard to class.
The following last names appear in more than one passenger class:
'Allen'
 'Brown'
 'Carlsson'
 'Carter'
 'Daly'
 'Davies'
 'Flynn'
 'Harper'
 'Harris'
 'Hart'
 'Keane'
 'Kelly'
 'Meyer'
 'Morley'
 'Smith'
 'Webber'
 'Williams'"""
)

st.write(
'''
# Titanic Visualization 2
'''
)
# Generate and display the figure
st.write("""
By far, the most prominent class of ticket sold was 3rd class (n=986, where 1st and 2nd classes totalled only 711). \n
Family group size analysis tell us that family groups of 7 or more exlusively purchased 3rd class tickets.\n
Was there an a discounted fare for group purchases?  i.e. Did larger families pay less per ticket?
""")
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)

st.write("It seems as though they priced tickets to encourage large family members in third class")

# st.write(
# '''
# # Titanic Visualization Bonus
# '''
# )
# # Generate and display the figure
# fig3 = visualize_family_size()
# st.plotly_chart(fig3, use_container_width=True)
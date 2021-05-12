							      	{% if post_item.liked == True %}
									  <form method="POST" action="{% url 'postlikes' post_item.id %}">
										  {% csrf_token %}
										<i type='submit' class="ri-thumb-up-fill"></i>
									  </form>
									{% else %}
									<a href="{% url 'postlikes' post_item.id %}"><i class="ri-thumb-up-line"></i>&ensp;</a>
									{% endif %}




									  	<form id="likebtn" action="{% url 'postlikes' post_item.id %}">
											{% if post_item.liked == True %}	  
											<button style="border: none; color: blue;" type="sumbit"><i class="ri-thumb-up-fill"></i></button>
											{% else %}
											<button style="border: none; color: blue;" type="sumbit"><i class="ri-thumb-up-line"></i></button>
											{% endif %}
										</form>
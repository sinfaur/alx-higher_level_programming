#include "lists.h"

/**
 * insert_node - inserts node in sorted list.
 * @head: Double pointer of listint_t type.
 * @number: Integer type.
 * Return: Address of the new node if success, NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		node->next = NULL;
		return (node);
	}

	temp = *head;
	while (temp->next != NULL)
	{
		if (number < temp->n)
		{
			node->next = temp;
			*head = node;
			return (node);
		}
		if (number <= temp->next->n)
		{
			node->next = temp->next;
			temp->next = node;
			return (node);
		}
		temp = temp->next;
	}
	node->next = NULL;
	temp->next = node;
	return (node);
}

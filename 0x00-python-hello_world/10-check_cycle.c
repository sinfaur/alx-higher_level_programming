#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list.
 * @list: listint_t type.
 * Return: 0 if no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp, *new;

	temp = list;
	new = list;

	while (temp != NULL && new != NULL &&new->next != NULL)
	{
		new = new->next->next;
		temp = temp->next;
		if (new == temp)
			return (1);
	}
	return (0);
}

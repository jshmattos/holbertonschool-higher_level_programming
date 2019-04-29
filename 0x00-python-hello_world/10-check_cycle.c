#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *tort = list;
	listint_t *hare = list;

	if (list == NULL)
		return (0);

	while (tort->next != NULL && hare->next->next != NULL)
	{
		tort = tort->next;
		hare = hare->next->next;
		if (tort == hare)
			return (0);
	}
	return (1);
}

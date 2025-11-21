import reflex as rx

from pcweb.components.icons.icons import get_icon
from typing import Optional

def product_card(
    number: int,
    name: str,
    title: str,
    description: str,
    link: Optional[str],
    url: Optional[str],
    color: tuple[str, str],
    graphic: str,
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(title, class_name="text-slate-12 text-xl font-semibold"),
            rx.el.span(description, class_name="text-slate-9 text-sm font-medium"),
            class_name="flex flex-col gap-2 px-10 pt-10",
        ),
        rx.el.div(
            rx.image(
                src=f"/landing/products/light/product_{graphic}.webp",
                class_name="w-auto pointer-events-none block dark:hidden",
            ),
            rx.image(
                src=f"/landing/products/dark/product_{graphic}.webp",
                class_name="w-auto pointer-events-none hidden dark:block",
            ),
            class_name="w-full max-h-[17.25rem] h-full overflow-hidden",
        ),
        rx.cond(
            link and url,
            rx.el.a(
                rx.el.span(
                    link,
                    class_name="text-sm font-medium text-slate-12 underline-none hover:text-slate-12",
                ),
                get_icon(
                    "chevron_right",
                    class_name="size-4 text-slate-9 group-hover:text-slate-12 group-hover:translate-x-1 transition-all duration-300",
                ),
                to=url,
                class_name="flex flex-row items-center gap-2 justify-between group h-[4rem] px-10 hover:bg-slate-2 transition-colors border-t max-lg:border-b border-slate-3",
            ),
        ),
        class_name="flex flex-col",
    )


def products() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.h2(
                "The Singularity Triad",
                class_name="text-slate-12 text-2xl lg:text-3xl font-semibold text-center",
            ),
            rx.el.p(
                "One system. Every device. Total resilience.",
                class_name="text-slate-9 text-lg font-medium text-center",
            ),
            class_name="flex flex-col items-center gap-2 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 lg:border-t px-10 py-12",
        ),
        rx.box(
            product_card(
                1,
                "Autonomous Defense Engine",
                "Autonomous Defense Engine",
                "Leverage AI-driven heuristics to detect and neutralize zero-day threats before they breach your perimeter.",
                "View Security Architecture",
                "#",
                ("violet", "9"),
                "ai",
            ),
            product_card(
                2,
                "Predictive Maintenance",
                "Predictive Maintenance",
                "Monitor hardware health from silicon to chassis. Predict component failures and automate maintenance workflows.",
                "Explore Forensics",
                "#",
                ("jade", "10"),
                "framework",
            ),
            product_card(
                3,
                "Global IoT Governance",
                "Global IoT Governance",
                "Manage millions of distributed devices—from edge sensors to orbital satellites—with military-grade encryption.",
                "View Deployment Models",
                "#",
                ("amber", "11"),
                "hosting",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 lg:divide-x divide-slate-3",
        ),
    )
